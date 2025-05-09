# scrape_lech_tickets.py
import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_lech_tickets(event_id=6244, output_path="sektor_summary.json"):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        url = f"https://bilety.lechpoznan.pl/Stadium/Index?eventId={event_id}"
        sectors_data = []

        def capture_response(response):
            if "GetWGLSectors" in response.url:
                sectors_data.append(response)

        page.on("response", capture_response)
        await page.goto(url)
        await page.wait_for_timeout(10000)

        parsed_sectors = []

        for response in sectors_data:
            try:
                json_data = await response.json()
                for sector in json_data.get("sectors", []):
                    name = sector.get("name")
                    trybuna = sector.get("platform")
                    level = sector.get("freeSeatsLevel", None)

                    if level is None:
                        status = "Brak danych"
                    elif level == 0:
                        status = "Wyprzedane"
                    elif level >= 30:
                        status = "Prawie pusta"
                    elif level >= 20:
                        status = "Mała liczba miejsc"
                    else:
                        status = "Dostępne"

                    parsed_sectors.append({
                        "trybuna": trybuna,
                        "sektor": name,
                        "poziom_dostepnosci": level,
                        "status": status
                    })
            except:
                continue

        await browser.close()

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(parsed_sectors, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(scrape_lech_tickets())
