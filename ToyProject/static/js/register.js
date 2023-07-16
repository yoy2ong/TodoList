function password_check(event) {
  var pwCheck = document.userInfo;

  if (pwCheck.password.value !== pwCheck.password2.value) {
    alert("비밀번호를 동일하게 입력하세요.");
    pwCheck.password.value = "";
    pwCheck.password2.value = "";
    event.preventDefault();
    return false;
  }

  return true;
}
