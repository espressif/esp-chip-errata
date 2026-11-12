"""Hover preview for links to errata description pages.

The preview is the rendered errata page: title, affected revisions, description
(including formulas), workaround, and solution. It is attached to ``:doc:``
links and to toctree entries, including the chip-revision tag pages.
"""

from __future__ import annotations

import posixpath
from urllib.parse import unquote

from docutils import nodes
from sphinx.util import logging
from sphinx.writers.html5 import HTML5Translator

logger = logging.getLogger(__name__)

ERRATA_DOC_PREFIX = '03-errata-description/'

# docname -> rendered HTML. Shared by every link to that page.
_previews = {}
# While rendering a preview, ignore links inside it so previews do not nest.
_rendering_preview = False


def _is_errata_page(docname: str) -> bool:
    # The description index includes every errata page, so it is not one bug.
    return (
        docname.startswith(ERRATA_DOC_PREFIX)
        and posixpath.basename(docname) != 'index'
    )


def _preview_id(docname: str) -> str:
    return 'errata-preview-' + docname.replace('/', '--')


def _docname_from_refuri(builder, fromdocname: str, refuri: str) -> str | None:
    if not refuri or '://' in refuri:
        return None
    path = refuri.split('#', 1)[0]
    if not path or path.startswith('#'):
        return None
    suffix = getattr(builder, 'link_suffix', '.html') or ''
    if path.startswith('/'):
        abs_uri = posixpath.normpath(path.lstrip('/'))
    else:
        from_uri = builder.get_target_uri(fromdocname)
        abs_uri = posixpath.normpath(posixpath.join(posixpath.dirname(from_uri), path))
    if suffix and abs_uri.endswith(suffix):
        abs_uri = abs_uri[:-len(suffix)]
    else:
        return None
    return unquote(abs_uri)


def _top_section(doctree):
    for child in doctree.children:
        if isinstance(child, nodes.section):
            return child
    return None


def _preview_html(builder, docname: str) -> str:
    global _rendering_preview
    if docname in _previews:
        return _previews[docname]

    html = ''
    env = builder.env
    try:
        # Drop a stale serialization so the preview matches the doctree on disk.
        cache = getattr(env, '_pickled_doctree_cache', None)
        if cache is not None:
            cache.pop(docname, None)
        doctree = env.get_and_resolve_doctree(docname, builder)
        section = _top_section(doctree)
        if section is not None:
            saved = (
                getattr(builder, 'current_docname', None),
                getattr(builder, 'imgpath', None),
                getattr(builder, 'dlpath', None),
            )
            _rendering_preview = True
            try:
                html = builder.render_partial(section.deepcopy()).get('fragment', '')
            finally:
                _rendering_preview = False
                builder.current_docname, builder.imgpath, builder.dlpath = saved
    except Exception:
        logger.debug('No errata preview for %s', docname, exc_info=True)
        html = ''

    html = html.strip()
    _previews[docname] = html
    return html


class ErrataTooltipTranslator(HTML5Translator):
    """HTML translator that embeds a full errata preview for description links."""

    def __init__(self, document, builder):
        super().__init__(document, builder)
        self._errata_previews = {}

    def visit_reference(self, node):
        if _rendering_preview:
            super().visit_reference(node)
            return
        fromdocname = self.builder.current_docname
        refuri = node.get('refuri', '')
        if not fromdocname:
            super().visit_reference(node)
            return
        docname = _docname_from_refuri(self.builder, fromdocname, refuri)
        if docname and _is_errata_page(docname):
            html = _preview_html(self.builder, docname)
            if html:
                preview_id = _preview_id(docname)
                self._errata_previews[preview_id] = html
                # The title is only an id. The script replaces it with the preview.
                node['reftitle'] = preview_id
                classes = node.setdefault('classes', [])
                if 'errata-preview' not in classes:
                    classes.append('errata-preview')
        super().visit_reference(node)

    def depart_document(self, node):
        for preview_id, html in self._errata_previews.items():
            self.body.append(f'<template id="{preview_id}">{html}</template>\n')
        super().depart_document(node)


def setup(app):
    app.set_translator('html', ErrataTooltipTranslator)
    app.add_css_file('errata-tooltip.css')
    app.add_js_file('errata-tooltip.js')
    return {
        'version': '1.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
