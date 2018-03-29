$(document).ready(function() {
    $("#userTool").click(function () {
        $("#profile-menu").toggle();
        $("#profile-menu-wrapper").toggle();
    });
    $("#profile-menu-wrapper").click(function () {
        $("#profile-menu").toggle();
        $("#profile-menu-wrapper").toggle();
    });
});