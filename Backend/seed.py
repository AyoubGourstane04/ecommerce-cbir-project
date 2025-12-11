import os.path
import random

from app import app
from database import db
from database.models import Product

products_data = [
    # --- Category: Electronics (Cluster: Cameras) ---
    {
        "name": "Canon EOS Rebel T7 DSLR Camera",
        "price": 479.99,
        "category": "Electronics",
        "description": "24.1 Megapixel CMOS (APS-C) sensor with fast auto-focus and built-in Wi-Fi.",
        "image_path": "static/images/canon_rebel_t7.jpg"
    },
    {
        "name": "Nikon D3500 DX-Format DSLR",
        "price": 496.95,
        "category": "Electronics",
        "description": "Compact, easy to use, and versatile. Features 24.2MP sensor and 1080p video recording.",
        "image_path": "static/images/nikon_d3500.jpg"
    },
    {
        "name": "Sony Alpha a6000 Mirrorless Camera",
        "price": 648.00,
        "category": "Electronics",
        "description": "World's fastest auto focus with 179 AF points and 11FPS. 24.3MP Exmor APS HD CMOS sensor.",
        "image_path": "static/images/sony_a6000.jpg"
    },
    {
        "name": "Fujifilm X-T30 II Mirrorless Camera",
        "price": 899.00,
        "category": "Electronics",
        "description": "Advanced X-Trans CMOS 4 sensor and X-Processor 4 engine. Vintage design with modern tech.",
        "image_path": "static/images/fuji_xt30.jpg"
    },

    # --- Category: Electronics (Cluster: Headphones) ---
    {
        "name": "Sony WH-1000XM5 Noise Canceling Headphones",
        "price": 348.00,
        "category": "Electronics",
        "description": "Industry-leading noise cancellation, crystal clear hands-free calling, and 30-hour battery life.",
        "image_path": "static/images/sony_xm5.jpg"
    },
    {
        "name": "Bose QuietComfort 45",
        "price": 329.00,
        "category": "Electronics",
        "description": "Iconic quiet, comfort, and sound. High-fidelity audio with adjustable EQ.",
        "image_path": "static/images/bose_qc45.jpg"
    },
    {
        "name": "Sennheiser Momentum 4 Wireless",
        "price": 299.95,
        "category": "Electronics",
        "description": "Audiophile-inspired sound system with 60-hour battery life.",
        "image_path": "static/images/sennheiser_m4.jpg"
    },

    # --- Category: Fashion (Cluster: Basic T-Shirts) ---
    {
        "name": "Nike Sportswear Club Tee",
        "price": 30.00,
        "category": "Fashion",
        "description": "Classic fit made of everyday cotton fabric. Features the iconic swoosh logo.",
        "image_path": "static/images/nike_tee_black.jpg"
    },
    {
        "name": "Adidas Adicolor Classics Trefoil Tee",
        "price": 35.00,
        "category": "Fashion",
        "description": "Authentic Adidas style. Soft cotton jersey feels comfortable for all-day wear.",
        "image_path": "static/images/adidas_trefoil_white.jpg"
    },
    {
        "name": "Puma Essentials Logo Tee",
        "price": 25.00,
        "category": "Fashion",
        "description": "Regular fit with PUMA No. 1 Logo rubber print at center chest.",
        "image_path": "static/images/puma_essentials_red.jpg"
    },
    {
        "name": "Under Armour Tech 2.0 Short Sleeve",
        "price": 25.00,
        "category": "Fashion",
        "description": "UA Tech fabric is quick-drying, ultra-soft & has a more natural feel.",
        "image_path": "static/images/ua_tech_blue.png"
    },

    # --- Category: Home (Cluster: Coffee Makers) ---
    {
        "name": "Keurig K-Elite Coffee Maker",
        "price": 189.99,
        "category": "Home",
        "description": "Single serve K-Cup pod coffee brewer with iced coffee capability and programmable features.",
        "image_path": "static/images/keurig_elite.jpg"
    },
    {
        "name": "Nespresso Vertuo Plus",
        "price": 159.00,
        "category": "Home",
        "description": "Coffee and Espresso Machine by De'Longhi. Brews 4 cup sizes.",
        "image_path": "static/images/nespresso_vertuo.jpg"
    },
    {
        "name": "Hamilton Beach FlexBrew Trio",
        "price": 99.85,
        "category": "Home",
        "description": "2-Way coffee maker. Brew a full pot using grounds or a single cup using a pod.",
        "image_path": "static/images/hamilton_flexbrew.jpg"
    },
    {
        "name": "Breville Barista Express Espresso Machine",
        "price": 749.95,
        "category": "Home",
        "description": "Dose control grinding with integrated conical burr grinder.",
        "image_path": "static/images/breville_barista.jpg"
    },

    # --- Category: Beauty (Cluster: Moisturizers) ---
    {
        "name": "CeraVe Moisturizing Cream",
        "price": 19.49,
        "category": "Beauty",
        "description": "Body and face moisturizer for dry skin with Hyaluronic Acid and Ceramides.",
        "image_path": "static/images/cerave_cream.jpg"
    },
    {
        "name": "Neutrogena Hydro Boost Water Gel",
        "price": 17.99,
        "category": "Beauty",
        "description": "Hydrating face moisturizer with hyaluronic acid for dry skin. Oil-free and non-comedogenic.",
        "image_path": "static/images/neutrogena_hydro.jpg"
    },
    {
        "name": "La Roche-Posay Toleriane Double Repair",
        "price": 22.99,
        "category": "Beauty",
        "description": "Face moisturizer with Ceramide-3, Niacinamide, Glycerin, and Prebiotic Thermal Water.",
        "image_path": "static/images/laroche_toleriane.jpg"
    },

    # --- Category: Toys (Cluster: Building Sets) ---
    {
        "name": "LEGO Star Wars X-Wing Fighter",
        "price": 49.99,
        "category": "Toys",
        "description": "Buildable toy playset featuring Luke Skywalker's iconic vehicle.",
        "image_path": "static/images/lego_xwing.png"
    },
    {
        "name": "LEGO Technic Ferrari 488 GTE",
        "price": 169.99,
        "category": "Toys",
        "description": "Endurance racer building kit. Highly detailed model for adults and kids.",
        "image_path": "static/images/lego_ferrari.png"
    },
    {
        "name": "Magna-Tiles Clear Colors 100-Piece Set",
        "price": 119.99,
        "category": "Toys",
        "description": "The original 3D magnetic building sets that engage young minds.",
        "image_path": "static/images/magnatiles_100.jpg"
    },

    # --- Category: Food (Cluster: Chocolates) ---
    {
        "name": "Lindt Excellence 70% Cocoa Dark Chocolate",
        "price": 4.59,
        "category": "Food",
        "description": "Full-bodied dark chocolate, masterfully crafted with the finest ingredients.",
        "image_path": "static/images/lindt_dark.png"
    },
    {
        "name": "Ferrero Rocher Hazelnut Chocolates (24 Count)",
        "price": 11.49,
        "category": "Food",
        "description": "A whole crunchy hazelnut in the center, a delicious creamy hazelnut filling, and a crisp wafer shell.",
        "image_path": "static/images/ferrero_24.jpg"
    },
    {
        "name": "Ghirardelli Intense Dark Chocolate Squares",
        "price": 5.99,
        "category": "Food",
        "description": "Sea Salt Soiree. A blend of dark chocolate and sea salt with roasted almonds.",
        "image_path": "static/images/ghirardelli_seasalt.png"
    },

    # --- Category: Sports (Cluster: Tennis Rackets) ---
    {
        "name": "Wilson Pro Staff 97 v13 Tennis Racket",
        "price": 249.00,
        "category": "Sports",
        "description": "Precision and classic feel. Used by Roger Federer.",
        "image_path": "static/images/wilson_prostaff.jpg"
    },
    {
        "name": "Babolat Pure Drive Tennis Racket",
        "price": 229.00,
        "category": "Sports",
        "description": "Explosive power and high stability. Great for baseline players.",
        "image_path": "static/images/babolat_puredrive.jpg"
    },
    {
        "name": "Head Speed MP Tennis Racket",
        "price": 239.00,
        "category": "Sports",
        "description": "Built for speed and a fast swing. Endorsed by Novak Djokovic.",
        "image_path": "static/images/head_speed.jpg"
    }
]

def seed_products():
    print("Seeding database...")

    print("1. Deleting old data...")
    try:
        db.session.query(Product).delete()
        db.session.commit()
        print("   Old data deleted.")
    except Exception as e:
        db.session.rollback()
        print(f"   Error deleting data: {e}")
        return

    print("2. Adding new products...")
    for item in products_data:
        # We don't need to check "if exists" because we just emptied the table!
        product = Product(
            name=item['name'],
            price=item['price'],
            category=item['category'],
            description=item['description'],
            image_path=item['image_path']
        )
        db.session.add(product)
        print(f"   Added: {item['name']}")

    try:
        db.session.commit()
        print("Database seeding completed.")
    except Exception as e:
        db.session.rollback()
        print(f"   Error committing data: {e}")

if __name__ == '__main__':
    # with app.app_context():
    seed_products()