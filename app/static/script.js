document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submit').addEventListener('click', function() {
        document.querySelector('.response').style.display = 'block';
    });
    document.getElementById('next').addEventListener('click', function() {
            location.reload();
        });
});
