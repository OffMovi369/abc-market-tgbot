from config import PAGES_DIR


def register_pages():
	for cog_file in PAGES_DIR.glob("*.py"):
		if cog_file.name != "__init__.py" and cog_file.name != "page.py":
			page = f'{cog_file.name[:-3]}'
			exec(f"from .{page} import {page}")
			exec(f"{page}.create_markup()")

register_pages()