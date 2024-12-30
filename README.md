# **To Do List**
---

## **Features**
- **Create**: Add new tasks to your ToDo list.
- **Read**: View all tasks and their statuses.
- **Update**:
  - Edit task details.
  - Toggle completion status of one or multiple tasks.
- **Delete**:
  - Delete selected tasks with a confirmation step.

---

## **Application Structure**

### **views.py**
| Function               | Purpose                            | URL Path                  |
|------------------------|------------------------------------|---------------------------|
| `task_list`            | View all tasks                    | `/tasks/`                 |
| `create_task`          | Create a new task                 | `/tasks/create/`          |
| `update_task`          | Edit a specific task              | `/tasks/<id>/update/`     |
| `toggle_task_status`   | Toggle completion status           | `/tasks/<id>/toggle/`     |
| `delete_task`          | Delete a specific task            | `/tasks/<id>/delete/`     |
| `delete_selected_tasks`| Confirm and delete multiple tasks | `/tasks/delete-selected/` |

---

## **CRUD Features**

### **Create**
- Add a new task using the "Create New Task" button on the main page.
- **URL**: `/tasks/create/`.

### **Read**
- View the list of tasks on the main page.
- **URL**: `/tasks/`.

### **Update**
- Edit a task using the "Edit" button next to each task.
- Toggle multiple tasks' statuses using the "Toggle Status" button.
- **URLs**:
  - `/tasks/<id>/update/`
  - `/tasks/<id>/toggle/`.

### **Delete**
- Delete multiple tasks after confirmation.
- **URLs**:
  - `/tasks/<id>/delete/`
  - `/tasks/delete-selected/`.

---

## **Pages and Links**

### **Main Page (`/`)**
- **Tasks Page** (`/tasks/`)
  - **Create Task Page** (`/tasks/create/`)
  - **Edit Task Page** (`/tasks/<id>/update/`)
  - **Toggle Task Status** (`/tasks/<id>/toggle/`)
  - **Delete Task Page** (`/tasks/<id>/delete/`)
  - **Delete Selected Tasks** (`/tasks/delete-selected/`)

---

## **Visual Overview**

### **Page Flow Diagram**
```
Main Page (/)
 ├── Create New Task ➡ /tasks/create/
 ├── Edit Task ➡ /tasks/<id>/update/
 ├── Toggle Task Status ➡ /tasks/<id>/toggle/
 └── Delete Selected ➡ /tasks/delete-selected/
 ```

## **Swagger Integration**
- The project includes Swagger for interactive API documentation.
### ***Swagger URLs***
- Swagger UI: http://127.0.0.1:8000/swagger/
=======
# 이융현 To-Do-List

## Features
- **Create**: Add new tasks.
- **Read**: View tasks and their statuses.
- **Update**: Toggle task completion and highlight important tasks.
- **Delete**: Remove tasks.
---
| Function            |	Purpose                       |	URL Path           |
|---------------------|-------------------------------|--------------------|
|task_list	          | View all tasks (read & toggle)|	/                  |
|create_task          |	Create a new task	            | /create/           |
|edit_task (optional) | Edit task details             | /update/id/      |
|delete_task          |	Delete a specific task        |	/delete-task/id/ |
|toggle_task_status   |	Toggle completion status      | /                  |
---
## CRUD Features
1. **Create**
- Add new tasks: Use the input field labeled "Enter a task" and click the "Add" button to add a task to the list.
- URL: /
2. **Read**
- View all tasks: Tasks are displayed in two sections: "Pending Tasks" and "Completed Tasks."
- URL: /
3. **Update**
- Toggle task completion status: Mark a task as completed by clicking its checkbox.
Highlight important tasks: Tasks entered with an asterisk (*) are marked as important and displayed at the top of the list.
- URL: /
4. **Delete**
- Delete a task: Remove a task by clicking the delete ("X") button next to it.
- URL: /
---
## **Pages and Links**
#### Main Page (/)
- Create New Task: Add tasks ➡ /
- Toggle Task Completion: Change task status ➡ /
- Delete Task: Remove tasks ➡ /
---
### **Visual Overview**
#### Page Flow Diagram
```
Main Page (/)
 ├── Add New Task ➡ /
 ├── Toggle Task Status ➡ /
 └── Delete Task ➡ /
```
---
### **How To Run**
1. Clone the repository:
```
git clone <repository-url>
```
2. Navigate to the project directory:
```
cd <project-folder>
```
3. Activate the virtual environment:
```
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Run the development server:
```
python manage.py runserver
```
