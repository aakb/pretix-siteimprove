from pretix.base.middleware import (
    SecurityMiddleware as BaseSecurityMiddleware, _merge_csp, _parse_csp,
    _render_csp,
)


class SecurityMiddleware(BaseSecurityMiddleware):
    def process_response(self, request, resp):
        h = {
            'script-src': [
                # Whitelist siteimprove urls in CSP.
                'https://siteimproveanalytics.com', 'https://*.siteimprove.com',
                # Whitelist cookieinformation urls and inline scripts.
                'https://*.cookieinformation.com', '\'unsafe-inline\'', '\'unsafe-eval\''
            ],
            'connect-src': ['https://*.cookieinformation.com'],
            'frame-src': ['https://*.cookieinformation.com'],
            'img-src': [
                'https://*.siteimprove.com',
                # The cookie consent form loads an image.
                'https://*.aarhus.dk'
            ],
            # Siteimprove adds inline styling.
            'style-src': ['\'unsafe-inline\''],
        }

        # Copied from super().process_response
        if 'Content-Security-Policy' in resp:
            _merge_csp(h, _parse_csp(resp['Content-Security-Policy']))
        resp['Content-Security-Policy'] = _render_csp(h)

        return super().process_response(request, resp)
