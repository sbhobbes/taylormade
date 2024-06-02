from flask import render_template
from datetime import datetime


def site():
    current_year = datetime.now().year
    
    return render_template('m_home_page.html', current_year=current_year)
