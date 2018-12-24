from flask import Blueprint, redirect, request, flash
import src.logger as log

routes = Blueprint('load', __name__, url_prefix='/load')


@routes.route('/new', methods=['POST'])
def file_upload_handler():
    return redirect('/')
