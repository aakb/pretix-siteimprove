from pretix.base.middleware import (
    SecurityMiddleware as BaseSecurityMiddleware, _merge_csp, _parse_csp,
    _render_csp,
)


class SecurityMiddleware(BaseSecurityMiddleware):
    def process_response(self, request, resp):
        h = {
            # Whitelist siteimprove urls in CSP.
            'script-src': ['https://siteimproveanalytics.com', 'https://*.siteimprove.com'],
            'img-src': ['https://*.siteimprove.com'],
            # Siteimprove adds inline styling.
            'style-src': ['\'unsafe-inline\''],
        }

        # Copied from super().process_response
        if 'Content-Security-Policy' in resp:
            _merge_csp(h, _parse_csp(resp['Content-Security-Policy']))
        resp['Content-Security-Policy'] = _render_csp(h)

        return super().process_response(request, resp)
