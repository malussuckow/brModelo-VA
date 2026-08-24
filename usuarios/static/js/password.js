document.querySelectorAll('.toggle-password').forEach(function (button) {
  button.addEventListener('click', function () {
    const wrapper = button.closest('.password-field');
    const input = wrapper.querySelector('input');
    const icon = button.querySelector('i');

    const isPassword = input.type === 'password';
    input.type = isPassword ? 'text' : 'password';

    icon.classList.toggle('fa-eye', !isPassword);
    icon.classList.toggle('fa-eye-slash', isPassword);
  });
});