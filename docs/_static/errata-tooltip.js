(function () {
    'use strict';

    var SHOW_DELAY_MS = 200;
    var HIDE_DELAY_MS = 120;
    var MATHJAX_URL = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';

    var tip = null;
    var showTimer = null;
    var hideTimer = null;
    var mathjaxLoading = null;

    function ensureTip() {
        if (tip) {
            return tip;
        }
        tip = document.createElement('div');
        tip.className = 'errata-preview-tip rst-content';
        tip.setAttribute('role', 'tooltip');
        tip.addEventListener('mouseenter', function () {
            clearTimeout(hideTimer);
        });
        tip.addEventListener('mouseleave', scheduleHide);
        document.body.appendChild(tip);
        return tip;
    }

    function hide() {
        clearTimeout(showTimer);
        clearTimeout(hideTimer);
        if (!tip) {
            return;
        }
        clearMath(tip);
        tip.classList.remove('visible');
        tip.replaceChildren();
    }

    function scheduleHide() {
        clearTimeout(hideTimer);
        hideTimer = setTimeout(hide, HIDE_DELAY_MS);
    }

    function place(anchor) {
        var el = ensureTip();
        var rect = anchor.getBoundingClientRect();
        var vw = document.documentElement.clientWidth;
        var vh = document.documentElement.clientHeight;

        el.style.visibility = 'hidden';
        el.style.left = '0px';
        el.style.top = '0px';
        el.style.maxWidth = Math.min(720, vw - 24) + 'px';
        el.classList.add('visible');

        var tipRect = el.getBoundingClientRect();
        var left = rect.left;
        if (left + tipRect.width > vw - 12) {
            left = vw - tipRect.width - 12;
        }
        if (left < 12) {
            left = 12;
        }

        var top = rect.bottom + 6;
        if (top + tipRect.height > vh - 12) {
            var above = rect.top - tipRect.height - 6;
            if (above >= 12) {
                top = above;
            }
        }

        el.style.left = left + 'px';
        el.style.top = top + 'px';
        el.style.visibility = 'visible';
    }

    function clearMath(el) {
        if (window.MathJax && window.MathJax.typesetClear) {
            try {
                window.MathJax.typesetClear([el]);
            } catch (e) {
                // The preview node may already have been emptied.
            }
        }
    }

    function ensureMathJax() {
        if (window.MathJax && window.MathJax.typesetPromise) {
            return Promise.resolve(window.MathJax);
        }
        if (mathjaxLoading) {
            return mathjaxLoading;
        }
        if (!window.MathJax) {
            window.MathJax = {
                tex: {
                    inlineMath: [['\\(', '\\)']],
                    displayMath: [['\\[', '\\]']]
                },
                startup: {typeset: false}
            };
        }
        mathjaxLoading = new Promise(function (resolve, reject) {
            var script = document.createElement('script');
            script.src = MATHJAX_URL;
            script.async = true;
            script.onload = function () {
                resolve(window.MathJax);
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
        return mathjaxLoading;
    }

    function rewriteUrls(root, pageUrl) {
        root.querySelectorAll('[href], [src]').forEach(function (el) {
            ['href', 'src'].forEach(function (attr) {
                var value = el.getAttribute(attr);
                if (!value || value.charAt(0) === '#' || value.indexOf('mailto:') === 0 || value.indexOf('://') !== -1) {
                    return;
                }
                try {
                    el.setAttribute(attr, new URL(value, pageUrl).href);
                } catch (e) {
                    // Leave a URL that the browser cannot resolve.
                }
            });
        });
    }

    function show(anchor) {
        var previewId = anchor.getAttribute('data-errata-preview');
        var template = previewId && document.getElementById(previewId);
        if (!template || !template.content) {
            return;
        }
        var el = ensureTip();
        clearMath(el);
        el.replaceChildren(template.content.cloneNode(true));
        el.querySelectorAll('a.headerlink, [id]').forEach(function (node) {
            if (node.classList.contains('headerlink')) {
                node.remove();
            } else {
                node.removeAttribute('id');
            }
        });
        try {
            rewriteUrls(el, new URL(anchor.getAttribute('href'), window.location.href).href);
        } catch (e) {
            // Relative links stay as built when the page URL cannot be resolved.
        }
        place(anchor);
        if (!el.querySelector('.math')) {
            return;
        }
        ensureMathJax().then(function (mathjax) {
            if (!tip || !tip.classList.contains('visible') || !mathjax.typesetPromise) {
                return;
            }
            return mathjax.typesetPromise([el]).then(function () {
                if (tip && tip.classList.contains('visible')) {
                    place(anchor);
                }
            });
        }).catch(function () {
            // Leave the TeX source visible when MathJax cannot be loaded.
        });
    }

    function bind(anchor) {
        var previewId = anchor.getAttribute('title');
        if (!previewId) {
            return;
        }
        anchor.setAttribute('data-errata-preview', previewId);
        anchor.removeAttribute('title');

        anchor.addEventListener('mouseenter', function () {
            clearTimeout(hideTimer);
            clearTimeout(showTimer);
            showTimer = setTimeout(function () {
                show(anchor);
            }, SHOW_DELAY_MS);
        });
        anchor.addEventListener('mouseleave', scheduleHide);
        anchor.addEventListener('focus', function () {
            clearTimeout(hideTimer);
            show(anchor);
        });
        anchor.addEventListener('blur', scheduleHide);
        anchor.addEventListener('click', hide);
    }

    function init() {
        document.querySelectorAll('a.errata-preview').forEach(bind);
        window.addEventListener('scroll', function (event) {
            if (tip && (event.target === tip || tip.contains(event.target))) {
                return;
            }
            hide();
        }, true);
        window.addEventListener('resize', hide);
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape') {
                hide();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
}());
