import os.path
import random

from Backend.app import app
from Backend.database import db
from Backend.database.models import Product

IMAGE_FOLDER = 'static/images/'
CATEGORIES = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Toys']

def seed_database():
    with app.app_context():
        db.create_all()

        if not os.path.exists(IMAGE_FOLDER):
            print(f"Error : {IMAGE_FOLDER} not found!")
            return

        images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f.lower() != 'default.png']

        if not images :
            print(f"Error : no images found in {IMAGE_FOLDER}!")
            return

        print(f"{len(images)} images found!")

        added_count = 0
        skipped_count = 0

        for img_name in images:
            relative_path = f"images/{img_name}"
            existing_product = Product.query.filter_by(image_path=relative_path).first()

            if existing_product:
                print(f"Skipped (already exists): {img_name}")
                skipped_count += 1
                continue

            category = random.choice(CATEGORIES)
            name = f"{category} Item - {img_name.split('.')[0].replace('_', ' ').title()}"
            price = round(random.uniform(10.0, 500.0), 2)
            description = f"This is a high-quality {category.lower()} product. Great value for the price!"

            new_product = Product(
                name=name,
                price=price,
                category=category,
                description=description,
                image_path=relative_path
            )

            db.session.add(new_product)
            added_count += 1
            print(f"Added: {name}")

        try:
            db.session.commit()
            print("-" * 30)
            print(f"Seeding Complete!")
            print(f"Added: {added_count} new products.")
            print(f"Skipped: {skipped_count} existing products.")
        except Exception as e:
            db.session.rollback()
            print(f"Error committing to database: {e}")

if __name__ == '__main__':
    seed_database()