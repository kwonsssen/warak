function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// unbind().bind() 더블클릭 방지
$(document).ready(function() {
    $('#signup_form').on("submit", addAnswer);
});

function addAnswer(e){
    e.preventDefault();  // 이벤트 진행 중지
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지
    var formData = $(this).serializeArray();
    let url = $(this).attr('action');
    let csrf = getCookie("csrftoken");
    formData = JSON.stringify(formData);
    $.ajax({
            type : 'POST', // post방식으로 전송
            url : url, // 서버로 보낼 url 주소
            data : {  // 서버로 보낼 데이터들 dict형식
            'formData':formData,
            'csrfmiddlewaretoken': csrf,
            },
            dataType:"json",
            // dataType : 'html',
            // 서버에서 리턴받아올 데이터 형식

            //서버에서 무사히 json데이터를 전달해주었다면
            success : function(response){
                if (response['result'] == true){
                  
                }else{
                    console.log(response['errors']['guardian_contact'][0])
                }
            },

            //서버에서 json데이터를 전달해주지 못했다면
            error : function(response){
                console.log("실패")
            },

    });
}
