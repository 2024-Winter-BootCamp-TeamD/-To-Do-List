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
