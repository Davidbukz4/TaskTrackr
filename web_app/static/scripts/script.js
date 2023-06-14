$(document).ready(function () {
  var userId = $("h1").attr("data-user-id");
  // global value to be used by cancelBtn
  var gTitle;
  var gDescription;
  var gDate;
  var gCompleted;

  // reload user tasks
  function reloadUserTasks() {
    $.ajax({
      url: "http://0.0.0.0:5001/api/v1/tasks/user/" + userId,
      method: "GET",
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
      success: function (response) {
        // Clear the task list
        $("#taskList").empty();

        // Iterate through the tasks and add them to the list
        response.forEach(function (task) {
          let fmtDate = new Date(task.due_date).toDateString();
          let taskStatus = task.completed
          if (taskStatus) {
            taskStatus = ' checked'
          } else {
            taskStatus = ''
          }
          var taskItem =
            "<li data-task-id=" +
            task.Task_id +
            ">" +
            "<h3>" +
            task.title +
            "</h3>" +
            "<p>" +
            task.description +
            "</p>" +
            "<p>Due Date: " +
            fmtDate +
            "</p>" +
            '<input type="checkbox" class="completedCheckbox"' + taskStatus + '>' +
            '<button class="editBtn">Edit</button>' +
            '<button class="deleteBtn">Delete</button>' +
            "</li>";
            // $('.completedCheckbox').prop('checked', task.completed);
          $("#taskList").append(taskItem);
        });

        highlightTasks();
      },
      error: function (xhr, status, error) {
        console.error("Error retrieving user tasks:", error);
      },
    });
  }
  // Reloads user tasks on page load
  //var userId = 1; // Replace with the actual user ID
  reloadUserTasks();

  // Handle adding a task
  $("#addTaskBtn").click(function () {
    const taskForm =
      '<div class="task-form">' +
      '<input type="text" class="task-title" placeholder="Title">' +
      '<input type="text" class="task-description" placeholder="Description">' +
      '<input type="date" class="task-due-date"><br>' +
      '<button class="saveTaskBtnPost">Save</button>' +
      '<button class="cancelTaskBtn">Cancel</button>' +
      "</div>";

    $("#taskList").prepend(taskForm);
    gTitle = "";
    gDescription = "";
    gDate = "";
  });

  // Handle saving a task
  $(document).on("click", ".saveTaskBtnPost", function () {
    const taskForm = $(this).parent();
    const title = taskForm.find(".task-title").val();
    const description = taskForm.find(".task-description").val();
    const dueDate = taskForm.find(".task-due-date").val();

    const formattedDueDate = new Date(dueDate).toISOString().split("T")[0];

    const taskData = {
      title: title,
      description: description,
      due_date: formattedDueDate,
    };

    $.ajax({
      url: "http://0.0.0.0:5001/api/v1/tasks/" + userId,
      method: "POST",
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
      data: JSON.stringify(taskData),
      contentType: "application/json",
      success: function (response) {
        console.log(response);
        fmtDate = new Date(response.due_date).toDateString();
        const taskItem =
          "<li data-task-id=" +
          response.id +
          ">" +
          "<h3>" +
          response.title +
          "</h3>" +
          "<p>" +
          response.description +
          "</p>" +
          "<p>Due Date: " +
          fmtDate +
          "</p>" +
          '<input type="checkbox" class="completedCheckbox">' +
          '<button class="editBtn">Edit</button>' +
          '<button class="deleteBtn">Delete</button>' +
          "</li>";

        taskForm.replaceWith(taskItem);
        highlightTasks()
      },
      error: function (xhr, status, error) {
        console.error("Error saving task:", error);
      },
    });
  });

  // Handle canceling a task
  $(document).on("click", ".cancelTaskBtn", function () {
    const taskForm = $(this).parent();
    const taskId = taskForm.data("task-id");
    const taskItem = $('#taskList li[data-task-id="' + taskId + '"]');

    const originalTitle = gTitle; //taskItem.find("h3").text();
    const originalDescription = gDescription; //taskItem.find("p:first-of-type").text();
    const originalDueDate = gDate;
    let originalCompleted = gCompleted; //taskItem
    if (originalCompleted) {
      originalCompleted = "checked"
    } else {
      originalCompleted = ""
    }

    let taskItemHtml =
      '<li data-task-id="' +
      taskId +
      '">' +
      "<h3>" +
      originalTitle +
      "</h3>" +
      "<p>" +
      originalDescription +
      "</p>" +
      "<p>Due Date: " +
      originalDueDate +
      "</p>" +
      '<input type="checkbox" class="completedCheckbox"' + originalCompleted + '>' +
      '<button class="editBtn">Edit</button>' +
      '<button class="deleteBtn">Delete</button>' +
      "</li>";

    if (gTitle == "" && gDescription == "" && gDate == "") {
      taskItemHtml = "";
    }
    taskForm.replaceWith(taskItemHtml);
  });

  // Handle editing a task
  $(document).on("click", ".editBtn", function () {
    const taskItem = $(this).parent();
    var taskId = taskItem.data("task-id");
    const title = taskItem.find("h3").text();
    const description = taskItem.find("p:first-of-type").text();
    const completed = taskItem.find(".completedCheckbox").prop("checked");
    const dueDate = taskItem
      .find("p:last-of-type")
      .text()
      .replace("Due Date: ", "");

    const editForm =
      '<div class="task-form" data-task-id=' +
      taskId +
      ">" +
      '<input type="text" class="task-title" value="' +
      title +
      '">' +
      '<input type="text" class="task-description" value="' +
      description +
      '">' +
      '<input type="date" class="task-due-date" value="' +
      dueDate +
      '">' +
      '<button class="saveTaskBtnPut">Save</button>' +
      '<button class="cancelTaskBtn">Cancel</button>' +
      "</div>";
    gTitle = title;
    gDescription = description;
    gDate = new Date(dueDate).toDateString();
    gCompleted = completed;

    taskItem.replaceWith(editForm);

    // Handle saving the edited task
    $(document).on("click", ".saveTaskBtnPut", function () {
      const editedTaskForm = $(this).parent();
      var taskId = editedTaskForm.data("task-id");
      const editedTitle = editedTaskForm.find(".task-title").val();
      const editedDescription = editedTaskForm.find(".task-description").val();
      const editedDueDate = editedTaskForm.find(".task-due-date").val();

      fmtDate = new Date(editedDueDate).toISOString().split("T")[0];
      const editedTaskData = {
        title: editedTitle,
        description: editedDescription,
        due_date: fmtDate,
      };

      $.ajax({
        url: "http://0.0.0.0:5001/api/v1/tasks/" + taskId,
        method: "PUT",
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
        data: JSON.stringify(editedTaskData),
        contentType: "application/json",
        success: function (response) {
          fmtDate = new Date(response.due_date).toDateString();
          const editedTaskItem =
            "<li data-task-id=" +
            response.id +
            ">" +
            "<h3>" +
            response.title +
            "</h3>" +
            "<p>" +
            response.description +
            "</p>" +
            "<p>Due Date: " +
            fmtDate +
            "</p>" +
            '<input type="checkbox" class="completedCheckbox">' +
            '<button class="editBtn">Edit</button>' +
            '<button class="deleteBtn">Delete</button>' +
            "</li>";

          editedTaskForm.replaceWith(editedTaskItem);
          highlightTasks()
        },
        error: function (xhr, status, error) {
          console.error("Error updating task:", error);
        },
      });
    });
  });

  // Handle deleting a task
  $(document).on("click", ".deleteBtn", function () {
    const taskItem = $(this).parent();
    var taskId = taskItem.data("task-id");
    $.ajax({
      url: "http://0.0.0.0:5001/api/v1/tasks/" + taskId,
      method: "DELETE",
      success: function (response) {
        console.log(response);
        taskItem.remove();
      },
      error: function (xhr, status, error) {
        console.error("Error deleting task:", error);
      },
    });
  });

  // Function to highlight tasks with due date reached
  function highlightTasks() {
    const today = new Date().toISOString().slice(0, 10);
    $("#taskList li").each(function () {
      let dueDate = $(this)
        .find("p:last-of-type")
        .text()
        .replace("Due Date: ", "");
      var date = new Date(dueDate);
      var year = date.getFullYear();
      var month = ("0" + (date.getMonth() + 1)).slice(-2);
      var day = ("0" + date.getDate()).slice(-2);

      // Format the date as yyyy-mm-dd
      dueDate = year + "-" + month + "-" + day;
      if (dueDate <= today) {
        $(this).css("background", "yellow");
      } else {
        $(this).css("background", "");
      }
    });
  }
});

$(document).on("change", ".completedCheckbox", function() {
  const taskItem = $(this).parent();
  const taskId = taskItem.data("task-id");
  const completed = $(this).prop("checked");

  // Send an AJAX request to update the completed status of the task
  $.ajax({
    url: "http://0.0.0.0:5001/api/v1/tasks/" + taskId,
    method: "PUT",
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    data: JSON.stringify({ completed: completed }),
    contentType: "application/json",
    success: function(response) {
      console.log(response)
    },
    error: function(xhr, status, error) {
      console.error("Error updating task completion status:", error);
    },
  });
});
