// APPOINTMENT DATA CONTROLLER
var appointmentDataController = (function () {
  var selectedItems;
  selectedItems = [];

  return {
    addItem: function (newItem) {
      var isItemExist;
      isItemExist = false;

      // check if newItem is existed
      selectedItems.forEach(function (item) {
        if (item === newItem) {
          return (isItemExist = true);
        }
      });

      if (!isItemExist) {
        // add newItem
        selectedItems.push(newItem);
      } else {
        // remove an exist Item
        selectedItems = selectedItems.filter(function (item) {
          return item !== newItem;
        });
      }
    },

    getSelectedItems: function () {
      return selectedItems;
    },

    removeSelectedItems: function () {
      while (selectedItems.length > 0) {
        selectedItems.pop();
      }
      console.log(selectedItems);
    },
  };
})();

// APPOINTMENT UI CONTROLLER
var appointmentUIController = (function () {
  var DOMstrings = {
    nameInput: 'contact-name',
    emailInput: 'contact-email',
    phoneInput: 'contact-phone',
    dateInput: 'datepicker',
    timeInput: 'timepicker',
    messageInput: 'contact-message',
  };

  return {
    getInput: function () {
      return {
        name: document.getElementById(DOMstrings.nameInput).value,
        email: document.getElementById(DOMstrings.emailInput).value,
        phone: document.getElementById(DOMstrings.phoneInput).value,
        date: document.getElementById(DOMstrings.dateInput).value,
        time: document.getElementById(DOMstrings.timeInput).value,
        message: document.getElementById(DOMstrings.messageInput).value,
      };
    },

    fieldValidation: function (inputObject) {
      var fieldInputs, message, selectedServices;
      fieldInputs = inputObject;
      message = '';
      selectedServices = appointmentDataController.getSelectedItems();
      for (var key in fieldInputs) {
        if (fieldInputs.hasOwnProperty(key)) {
          if (key == 'name' && fieldInputs[key] == '') {
            message = 'Please provide complete information into the form below';
          }
          if (key == 'phone' && fieldInputs[key] == '') {
            message = 'Please provide complete information into the form below';
          }
          if (key == 'date' && fieldInputs[key] == '') {
            message = 'Please provide complete information into the form below';
          }
          if (key == 'time' && fieldInputs[key] == '') {
            message = 'Please provide complete information into the form below';
          }
        }
      }
      if (selectedServices.length === 0) {
        message = 'Please provide complete information into the form below';
      }

      return message;
    },

    getDOMstring: function () {
      return DOMstrings;
    },

    clearFields: function () {
      var fields = DOMstrings;
      for (var key in fields) {
        if (fields.hasOwnProperty(key)) {
          document.getElementById(fields[key]).value = '';
        }
      }
    },
  };
})();

// APPOINTMENT CONTROLLER
var appointmentController = (function () {
  var fieldInputs, selectedServices, validationError, checkboxIDs;
  checkboxIDs = [];
  var setEventListeners = function () {
    document
      .getElementById('service-container')
      .addEventListener('click', selectCheckBox);

    document
      .getElementById('submit__btn')
      .addEventListener('click', function () {
        // make an appointment happens here
        // collect all input data
        fieldInputs = appointmentUIController.getInput();
        selectedServices = appointmentDataController.getSelectedItems();

        // disappear any existing notification if have
        var alert = document.getElementById('validation-alert');
        if (alert) {
          document.getElementById('validation-alert').style.display = 'none';
        }

        // check input validation
        validationError = appointmentUIController.fieldValidation(fieldInputs);

        if (validationError !== '') {
          var alertHtml =
            '<div class="alert alert-warning alert-dismissible text-center" id="validation-alert" role="alert"><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span></button><strong style="color: red">%content%</strong></div>';

          newAlertHtml = alertHtml.replace('%content%', validationError);

          if (document.getElementById('validation-alert') !== null) {
            console.log('2');
            var elem = document.getElementById('validation-alert');
            elem.parentNode.removeChild(elem);
            document
              .getElementById('before-make-appointment')
              .insertAdjacentHTML('beforebegin', newAlertHtml);
            setTimeout(function () {
              var elem = document.getElementById('validation-alert');
              elem.parentNode.removeChild(elem);
            }, 5000);
          } else {
            console.log('1');
            document
              .getElementById('before-make-appointment')
              .insertAdjacentHTML('beforebegin', newAlertHtml);
            setTimeout(function () {
              var elem = document.getElementById('validation-alert');
              elem.parentNode.removeChild(elem);
            }, 5000);
          }
        } else {
          // submit payload
          submitPayload();
        }

        // clear all field and checkbox

        // popup a notification
      });
  };

  var submitPayload = function () {
    var httpRequest = new XMLHttpRequest();
    var csrf_token = document.querySelector('input[name=csrfmiddlewaretoken]')
      .value;

    if (!httpRequest) {
      console.log('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }

    httpRequest.onreadystatechange = alertContents;
    httpRequest.open('POST', '/appointments');
    httpRequest.setRequestHeader(
      'Content-Type',
      'application/x-www-form-urlencoded'
    );
    httpRequest.setRequestHeader('X-CSRFToken', csrf_token);

    var dataObject = {
      inputs: fieldInputs,
      selectedServices: selectedServices,
    };

    var dataString = JSON.stringify(dataObject);

    httpRequest.send('data=' + dataString);

    function alertContents() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
          var responseText = JSON.parse(httpRequest.responseText);

          // clear input fields
          appointmentUIController.clearFields();
          // clear checkboxes
          checkboxIDs.forEach(function (Id) {
            if (document.getElementById(Id).checked == true) {
              document.getElementById(Id).checked = false;
            }
          });

          // clear checkboxIDs
          checkboxIDs = [];

          // remove all selected services from data controller
          appointmentDataController.removeSelectedItems();

          var alertHtml =
            '<div class="alert alert-success alert-dismissible text-center" id="success-alert" role="alert"><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span></button><strong>%content%</strong></div>';

          newAlertHtml = alertHtml.replace('%content%', responseText.success);
          document
            .getElementById('before-make-appointment')
            .insertAdjacentHTML('beforebegin', newAlertHtml);
          setTimeout(function () {
            document.getElementById('success-alert').style.display = 'none';
          }, 5000);
        } else {
          console.log('There was a problem with the request.');
        }
      }
    }
  };

  var selectCheckBox = function (event) {
    // get id element of event target
    var itemID, splitID, ID, labelID, serviceItem, checkBox;
    if (event.target.tagName.toLowerCase() == 'input') {
      itemID = event.target.getAttribute('id');
      checkBox = document.getElementById(itemID);
      // add checkbox ID to an array
      if (checkBox.checked == true) {
        checkboxIDs.unshift(itemID);
      } else {
        checkboxIDs.shift(itemID);
      }

      if (itemID) {
        splitID = itemID.split('-');
        ID = splitID[1];

        // create ID element for label tag
        labelID = 'labelforcheckbox-' + ID;

        // get label value
        serviceItem = document.getElementById(labelID).textContent;

        appointmentDataController.addItem(serviceItem);
      }
    }
  };

  return {
    init: function () {
      console.log('application has started.');
      setEventListeners();
    },
  };
})();

appointmentController.init();
