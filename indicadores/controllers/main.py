import logging

from odoo import http
from odoo.http import request

import json
import qrcode
import base64


class MainController(http.Controller):

    _logger = logging.getLogger(__name__)

	@http.route(['/indicadores'], auth='public', website=True)
	return http.request.render('indicadores.inicio_indicador')