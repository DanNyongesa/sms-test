from flask import render_template, Blueprint,redirect, flash, url_for, abort
from ..models import Topic, Screen

from .forms import Add_ScreenForm, Add_TopicForm, Edit_ScreenForm, Edit_TopicForm
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('topics')
def get_topics():
    topics = Topic.query.all()
    return render_template('topics.html', topics=topics)


@main.route('topics/<string:slug>')
def get_topic(slug):
    topic = Topic.by_slug(slug)
    return render_template('topic.html', topic=topic)


@main.route('topics/<string:slug>/edit', methods=['get', 'post'])
def edit_topic(slug):
    topic = Topic.by_slug(slug)
    form = Edit_TopicForm()
    if form.validate_on_submit():
        topic.title = form.title.data
        topic.save()
        flash('Topic edited', category='success')
        return redirect(url_for('.get_topic', slug=topic.slug))
    form.title.data = topic.title
    return render_template('edit_topic.html', form=form)


@main.route('topics/add', methods=['get', 'post'])
def add_topic():
    form = Add_TopicForm()
    if form.validate_on_submit():
        topic = Topic.create(title=form.title.data)
        flash('Topic added', category='success')
        return redirect(url_for('.get_topic', slug=topic.slug))
    return render_template('add_topic.html', form=form)


@main.route('topics/<string:slug>/delete', methods=['get', 'post'])
def delete_topic(slug):
    topic =Topic.by_slug(slug)
    topic.delete()
    flash('Topic removed', category='info')
    return redirect(url_for('.get_topics'))


@main.route('topics/<int:id>/edit-screen', methods=['get', 'post'])
def edit_screen(id):
    screen = Screen.by_id(id)
    topic = screen.topic
    if screen is None:
        return abort(404)
    form = Edit_ScreenForm()
    if form.validate_on_submit():
        screen.text = form.text.data
        screen.save()
        flash('Screen Edited', category='success')
        return redirect(url_for('.get_topic', slug=screen.topic.slug))
    form.text.data = screen.text
    return render_template('edit_screen.html', form=form, topic=topic)


@main.route('topics/<int:id>/delete-screen', methods=['get', 'post'])
def delete_screen(id):
    screen = Screen.by_id(id)
    if screen is None:
        return abort(404)
    topic = screen.topic
    screen.delete()
    flash('Screen removed', category='warning')
    return redirect(url_for('.get_topic', slug=topic.slug))

@main.route('topics/<string:slug>/add-screen', methods=['get', 'post'])
def add_screen(slug):
    topic = Topic.by_slug(slug)
    form = Add_ScreenForm()
    if form.validate_on_submit():
        screen = Screen.create(topic=topic, text=form.text.data)
        flash("Screen Added", category='success')
        return redirect(url_for('.get_topic', slug=topic.slug))
    return render_template('add_screen.html', form=form, topic=topic)
