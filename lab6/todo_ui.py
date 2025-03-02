import datetime
import requests
import streamlit as st

url = 'http://localhost:8000'

def get_tasks():
    r = requests.get(f'{url}/tasks')
    if (r.status_code == 404): return []
    return r.json()['tasks']

@st.dialog("Add new task")
def add_task(completed_def):
    title = st.text_input("Title", max_chars=256)
    if (title == ""):
        st.write("Title can't be empty")
    description = st.text_input("Description")
    completed = st.checkbox("Completed", value=completed_def)
    has_deadline = st.checkbox("Has deadline")
    if (has_deadline):
        deadline_val = datetime.datetime.now()
        deadline = st.date_input("Deadline", value=deadline_val)
        
    cols = st.columns(5)
    if cols[0].button("Add", type="primary", disabled = title == ""):
        task_data = {"title":title, "description":description, "completed":completed}
        if (has_deadline):
            task_data['deadline'] = deadline.isoformat()
        r = requests.post(f'{url}/tasks/', json=task_data)
        if (r.status_code == 200):
            st.rerun()
        else:
            st.write('Something went wrong, try again.')
    if cols[1].button("Cancel"):
        st.rerun()


@st.dialog("Edit your task")
def edit(task_id, title_val, description_val, completed_val, datetime_val):
    title = st.text_input("Title", value = title_val, max_chars=256)
    description = st.text_input("Description", value = description_val)
    completed = st.checkbox("Completed", value=completed_val)
    has_deadline = st.checkbox("Has deadline", value=datetime_val != None, disabled=datetime_val!=None)
    if (has_deadline):
        deadline_val = datetime.datetime.fromisoformat(datetime_val) if datetime_val != None else datetime.datetime.now()
        deadline = st.date_input("Deadline", value=deadline_val)
        
    cols = st.columns(5)
    if cols[0].button("Edit", type="primary"):
        task_data = {"title":title, "description":description, "completed":completed}
        if (has_deadline):
            task_data['deadline'] = deadline.isoformat()
        r = requests.put(f'{url}/tasks/{task_id}', json=task_data)
        if (r.status_code == 200):
            st.rerun()
        else:
            st.write('Something went wrong, try again.')
    if cols[1].button("Cancel"):
        st.rerun()

@st.dialog("Delete task")
def remove(task_id, title_val):
    st.subheader(f"Are you sure you want to delete the task\"{title_val}\"?")
    st.write("This action cannot ba undone.")
    cols = st.columns(5)
    if cols[0].button("Delete", type="primary"):
        r = requests.delete(f'{url}/tasks/{task_id}')
        if (r.status_code == 200):
            st.rerun()
        else:
            st.write('Something went wrong, try again.')
    if cols[1].button("Cancel"):
        st.rerun()

if __name__ == '__main__':
    st.title("Todo list app")
    col_incomplete, col_completed = st.columns(2)
    tasks = get_tasks()
    col_incomplete.header('Incomplete')
    col_incomplete.divider()
    if col_incomplete.button("Add task", key="at0", use_container_width=True):
        add_task(False)
    col_completed.header('Completed')
    col_completed.divider()
    if col_completed.button("Add task", key="at1", use_container_width=True):
        add_task(True)
    incomp = False
    comp = False
    for task in tasks:
        if (task['completed']):
            c = col_completed.container(border=True)
            comp = True
        else:
            c = col_incomplete.container(border=True)
            incomp = True
        c.markdown(f'##### {task['title']}')
        c.write(task['description'])
        c.checkbox("Completed", value = task['completed'], disabled=True, key=f"completed_{task['id']}")
        if (task['deadline']):
            c.write(' '.join(task['deadline'].split('T')))
        cb = c.container(key=f"task_buttons_{task['id']}")
        if (cb.button("Edit", key=f"edit_{task['id']}")):
            edit(task['id'], task['title'], task['description'], task['completed'], task['deadline'])
        if (cb.button("Remove", key=f"remove_{task['id']}", type="primary")):
            remove(task['id'], task['title'])
    
    if incomp:
        if col_incomplete.button("Add task", key="at2", use_container_width=True):
            add_task(False)
    if comp:
        if col_completed.button("Add task", key="at3", use_container_width=True):
            add_task(True)
        