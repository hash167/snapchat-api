ACTIVATE := . venv/bin/activate &&

venv:
	@python3 -m venv venv

refresh:
	@$(ACTIVATE) python snapchat_refresh_token.python
