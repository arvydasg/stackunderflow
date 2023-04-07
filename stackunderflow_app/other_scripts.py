"""Keeping other scripts here that are used for the project."""

import os
import secrets
from PIL import Image
from stackunderflow_app.app import app


def save_picture(form_picture):
    """Being used for account images."""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_images", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
