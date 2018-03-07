from pretix.base.middleware import SecurityMiddleware as BaseSecurityMiddleware


class SecurityMiddleware(BaseSecurityMiddleware):
    def process_response(self, request, resp):
        # Whitelist siteimprove urls in CSP.
        h = {
            'script-src': ['https://siteimproveanalytics.com', 'https://*.siteimprove.com'],
            'img-src': ['https://*.siteimprove.com'],
        }
        resp['Content-Security-Policy'] = "; ".join(k + ' ' + ' '.join(v) for k, v in h.items())

        return super().process_response(request, resp)
