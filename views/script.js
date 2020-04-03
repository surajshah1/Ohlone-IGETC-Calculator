
var options = {
    valueNames: ['cname']
}

var courses = new List('courses', options);

var coursefield = $('#cname-field');
var addBtn = $('#add-btn');

 addBtn.click(function() {
    console.log(coursefield.val);
    courses.add({
         course: coursefield.val()
     })
 })

