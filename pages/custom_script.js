var submittedTextList = [];

window.onload = function() {
    document.getElementById('submit-button').addEventListener('click', function() {
        var user_input = document.getElementById('user-input').value;
        if (user_input.trim() !== '') {
            submittedTextList.push(user_input);
            var submittedTextContainer = document.getElementById('submitted-text-container');
            submittedTextContainer.innerHTML = "<br>User Submissions:<br>";
            for (var i = 0; i < submittedTextList.length; i++) {
                submittedTextContainer.innerHTML += "<br>" + submittedTextList[i] + "<br>" + '='.repeat(40) + "<br>";
            }
            document.getElementById('user-input').value = '';  // Clear the user input
        }
    });
}
