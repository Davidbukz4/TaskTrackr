$(document).ready(function () {
  // Handle adding a task
  $('#addTaskBtn').click(function () {
    const taskForm =
      '<div class="task-form">' +
      '<input type="text" class="task-title" placeholder="Title">' +
      '<input type="text" class="task-description" placeholder="Description">' +
      '<input type="date" class="task-due-date"><br>' +
      '<button class="saveTaskBtn">Save</button>' +
      '<button class="cancelTaskBtn">Cancel</button>' +
      '</div>';

    $('#taskList').prepend(taskForm);
  });

  // Handle saving a task
  $(document).on('click', '.saveTaskBtn', function () {
    const taskForm = $(this).parent();
    const title = taskForm.find('.task-title').val();
    const description = taskForm.find('.task-description').val();
    const dueDate = taskForm.find('.task-due-date').val();

    const taskItem =
      '<li>' +
      '<h3>' +
      title +
      '</h3>' +
      '<p>' +
      description +
      '</p>' +
      '<p>Due Date: ' +
      dueDate +
      '</p>' +
      '<button class="editBtn">Edit</button>' +
      '<button class="deleteBtn">Delete</button>' +
      '</li>';

    taskForm.replaceWith(taskItem);
  });

  // Handle canceling a task
  $(document).on('click', '.cancelTaskBtn', function () {
    const taskForm = $(this).parent();
    const title = taskForm.find('.task-title').val();
    const description = taskForm.find('.task-description').val();
    const dueDate = taskForm.find('.task-due-date').val();

    const taskItem =
      '<li>' +
      '<h3>' +
      title +
      '</h3>' +
      '<p>' +
      description +
      '</p>' +
      '<p>Due Date: ' +
      dueDate +
      '</p>' +
      '<button class="editBtn">Edit</button>' +
      '<button class="deleteBtn">Delete</button>' +
      '</li>';
    if (title || description || dueDate) {
      taskForm.replaceWith(taskItem);
    } else {
      taskForm.replaceWith('');
    }
  });

  // Handle editing a task
  $(document).on('click', '.editBtn', function () {
    const taskItem = $(this).parent();
    const title = taskItem.find('h3').text();
    const description = taskItem.find('p:first-of-type').text();
    const dueDate = taskItem
      .find('p:last-of-type')
      .text()
      .replace('Due Date: ', '');

    const editForm =
      '<div class="task-form">' +
      '<input type="text" class="task-title" value="' +
      title +
      '">' +
      '<input type="text" class="task-description" value="' +
      description +
      '">' +
      '<input type="date" class="task-due-date" value="' +
      dueDate +
      '">' +
      '<button class="saveTaskBtn">Save</button>' +
      '<button class="cancelTaskBtn">Cancel</button>' +
      '</div>';

    taskItem.replaceWith(editForm);
  });

  // Handle deleting a task
  $(document).on('click', '.deleteBtn', function () {
    $(this).parent().remove();
  });

  // Highlight tasks with due date reached
  const today = new Date().toISOString().slice(0, 10);
  $('#taskList li').each(function () {
    const dueDate = $(this)
      .find('p:last-of-type')
      .text()
      .replace('Due Date: ', '');
    if (dueDate <= today) {
      $(this).addClass('highlight');
    }
  });
});
