from flask import Blueprint, render_template
from .web_srapping import Facebook,Tesla,Amazon,Google,Apple,Microsoft,Netflix,df1
import matplotlib.pyplot as plt

views = Blueprint('views', __name__)

@views.route('/')

def home():

    return render_template('home.html')
@views.route('/about')
def about():
    
    return render_template('about.html')
@views.route('/FB')
def FB():
    
    return render_template('facebook.html',column_names=Facebook.columns.values, row_data=list(Facebook.values.tolist()),zip=zip)
@views.route('/TSLA')
def TSLA():
   
    return render_template('tesla.html',column_names=Tesla.columns.values, row_data=list(Tesla.values.tolist()),zip=zip)
@views.route('/AMZN')
def AMZN():
    
    return render_template('amazon.html',column_names=Amazon.columns.values, row_data=list(Amazon.values.tolist()),zip=zip)
@views.route('/GOOGL')
def GOOGL():
    
    return render_template('google.html',column_names=Google.columns.values, row_data=list(Google.values.tolist()),zip=zip)
@views.route('/AAPL')
def AAPL():
    
    return render_template('apple.html',column_names=Apple.columns.values, row_data=list(Apple.values.tolist()),zip=zip)
@views.route('/MSFT')
def MSFT():

    return render_template('microsoft.html',column_names=Microsoft.columns.values, row_data=list(Microsoft.values.tolist()),zip=zip)
@views.route('/NTFLX')
def NTFLX():
    
    return render_template('netflix.html',column_names=Netflix.columns.values, row_data=list(Netflix.values.tolist()),zip=zip)
@views.route('/tracker')
def tracker():
    df2  = df1.groupby(['market', 'date']).mean().unstack()
    df2  = df2.xs('compound', axis="columns").transpose()
    df2.plot(kind='bar',figsize=(16,8),width=1.5)   
    plt.savefig('website/static/images/my_plot.png',transparent=True)

    return render_template('tracker.html',name = '', url ='/static/images/my_plot.png')
