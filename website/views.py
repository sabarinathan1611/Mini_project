from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, current_app, make_response
from flask_login import login_required, current_user
views = Blueprint('views', __name__)