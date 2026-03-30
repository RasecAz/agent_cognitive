import webbrowser

class DeviceService:

    def __init__(self):
        self.market_links = {
            "word": "https://play.google.com/store/apps/details?id=com.microsoft.office.word",
            "pdf": "https://play.google.com/store/apps/details?=com.adobe.reader"
        }

    def abrir_app_o_tienda(self, app_name: str):
        url = self.market_links.get(app_name.lower())
        if url:
            print(f"--- [SISTEMA]: Abriendo navegador en: {url} ---")
            webbrowser.open(url)
            return True
        return False
            


