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
|edit_task (optional) | Edit task details             | /update/<id>/      |
|delete_task          |	Delete a specific task        |	/delete-task/<id>/ |
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
