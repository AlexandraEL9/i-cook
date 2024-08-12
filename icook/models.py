from icook import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    img_src = db.Column(db.String(255), nullable=True)
    directions = db.Column(db.Text, nullable=False)
    # Add a foreign key if linked to another table, e.g., Category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.recipe_name}>"