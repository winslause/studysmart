document.addEventListener('DOMContentLoaded', () => {
  console.log('admin_portal.js loaded successfully');

  const deleteButtons = document.querySelectorAll('.delete-question');
  console.log(`Found ${deleteButtons.length} delete buttons`);

  if (deleteButtons.length === 0) {
    console.warn('No delete buttons found. Check if questions are rendered and buttons have .delete-question class.');
  }

  deleteButtons.forEach((button, index) => {
    const questionId = button.getAttribute('data-question-id');
    const questionTitle = button.getAttribute('data-question-title');

    // Log button attributes for debugging
    console.log(`Button ${index + 1}: ID=${questionId}, Title=${questionTitle}`);

    if (!questionId || !questionTitle) {
      console.error(`Button ${index + 1} has invalid attributes: ID=${questionId}, Title=${questionTitle}`);
      return;
    }

    button.addEventListener('click', () => {
      console.log(`Delete button clicked: ID=${questionId}, Title=${questionTitle}`);

      const questionIdInput = document.getElementById('delete_question_id');
      const questionTitleSpan = document.getElementById('delete_question_title');

      if (!questionIdInput || !questionTitleSpan) {
        console.error('Modal elements missing: delete_question_id or delete_question_title not found');
        return;
      }

      questionIdInput.value = questionId;
      questionTitleSpan.textContent = questionTitle;
      console.log(`Modal populated: ID=${questionId}, Title=${questionTitle}`);
    });
  });

  const deleteForm = document.getElementById('deleteQuestionForm');
  if (deleteForm) {
    deleteForm.addEventListener('submit', (e) => {
      const formData = new FormData(deleteForm);
      const formEntries = Object.fromEntries(formData);
      console.log('Delete form submitted with data:', formEntries);

      if (!formEntries.question_id) {
        console.error('Form submission failed: question_id is missing');
        e.preventDefault(); // Prevent submission if question_id is missing
      }
      if (!formEntries.action) {
        console.error('Form submission failed: action is missing');
        e.preventDefault();
      }
      if (!formEntries.csrfmiddlewaretoken) {
        console.error('Form submission failed: csrfmiddlewaretoken is missing');
        e.preventDefault();
      }
    });
  } else {
    console.error('Delete form not found: #deleteQuestionForm');
  }
});