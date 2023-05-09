## admin.py
    CustomUserAdmin 클래스에서는 UserAdmin 클래스를 상속받아서 우리가 원하는대로 사용자 목록을 구성하였습니다. add_form 속성에는 회원가입 폼으로 SignUpForm을 사용하도록 지정하였고, list_display 속성에는 유저 목록에서 보일 필드들을 지정하였습니다. fieldsets 속성에서는 회원가입, 유저 정보 수정 시 필요한 필드들을 그룹으로 묶어서 보여줌으로써 UI를 개선하였습니다. 그 외에도 필터링 옵션, 다대다 관계에서 선택 가능한 필드들의 표시 방식 설정 등을 지정하였습니다. 마지막으로 MyUser 모델을 CustomUserAdmin으로 등록하여 우리가 원하는대로 동작하도록 하였습니다.

## forms.py
    회원가입 폼과 로그인 폼이 정의된 파일입니다.

## models.py
    django.contrib.auth.models의 AbstractBaseUser와 BaseUserManager를 상속받아 새로운 유저 모델인 MyUser와 유저 모델을 관리하는 MyUserManager를 정의하였습니다.

    MyUserManager 클래스는 유저 모델의 생성과 관리를 담당합니다. create_user() 메소드는 이메일과 패스워드를 받아 새로운 유저를 생성합니다. create_superuser() 메소드는 create_user()를 호출하여 새로운 슈퍼유저를 생성합니다.

    MyUser 클래스는 AbstractBaseUser를 상속받아 구현한 사용자 모델입니다. 사용자 모델의 필드로는 이메일, 닉네임, MBTI 등이 있으며, is_active, is_admin 등의 boolean 필드도 있습니다. USERNAME_FIELD는 이메일 필드를 지정합니다.

    has_perm()과 has_module_perms()는 권한 체크에 사용되는 메소드로, 현재 유저가 특정 권한을 가지고 있는지를 반환합니다. is_staff는 유저가 관리자인지를 나타내는 속성으로 is_admin 값과 동일합니다. 이 부분에 관해서는 추후 세부적인 구현을 할 예정입니다.

## views.py
    회원가입, 로그인, 로그아웃을 처리하는 뷰가 있습니다. 오류 수정을 거쳐 회원가입 후 로그인을 유지하며 완료 페이지(로그인된 이메일 표시)를 보여주는 뷰, 로그인하지 않은 사용자에게 표시하는 home 페이지를 보여주는 뷰 등을 추가로 정의하였습니다.