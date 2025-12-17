
from playwright.sync_api import sync_playwright
import time

def verify_map_tiles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Grant clipboard permissions
        context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
        page = context.new_page()

        # Set cookie to simulate admin login
        # In admin/page.tsx: const token = getCookie("admin_token");
        context.add_cookies([{
            "name": "admin_token",
            "value": "dummy_token_for_verification",
            "domain": "localhost",
            "path": "/"
        }])

        try:
            # Navigate to admin page
            page.goto("http://localhost:3000/admin")

            # Wait for the admin page to load
            page.wait_for_selector("text=Administration O2Paris", state="visible")

            # Click on "Configuration" tab
            page.get_by_text("Configuration").click()

            # Click on "Voir tous les styles" to expand the list
            page.get_by_text("Voir tous les styles").click()

            # Wait for the tile options to appear
            page.wait_for_selector("text=OpenStreetMap France", state="visible")

            # Take a screenshot of the map tiles
            page.screenshot(path="verification/map_tiles.png", full_page=True)
            print("Screenshot taken: verification/map_tiles.png")

            # Also log the visible options to verify we have the new ones
            options = page.locator(".grid.grid-cols-2.md\\:grid-cols-4.gap-3 button").all_inner_texts()
            print("Found options:")
            for opt in options:
                print(f"- {opt.replace('\n', ' ')}")

        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="verification/error.png")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_map_tiles()
