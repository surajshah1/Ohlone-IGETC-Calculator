var React = require('react');

class CourseList extends React.Component {
  render() {
    var styles = {
      border: "1px solid black",
      color: "green"
    }
    var style2 = {
      //backgroundColor: "yellow",
      textAlign: "center"
    }
    var style3 = {
      backgroundColor: "yellow",
      border: "1px solid black"
    }
    var areaobject = this.props.areaobj;

    function completed () {
      if (Object.keys(areaobject).length == 1 && Object.keys(areaobject)[0].includes("Area 7")) {
        return (<p>Congratulations you have completed IGETC for UC</p>)
      }
    }
    var itemstable = Object.keys(areaobject).map(function(item) {
      //console.log(item);
      return (<tr> <td style = {styles}>{item} </td> <td style = {styles}> {areaobject[item].map(function(course) {
            return <var> {course} | </var>})} </td> </tr>
      )
    });
    return (
      <div className ="areas" style = {style2}>
      <h1>Area List</h1>
      <table style = {style3}>
        <th style = {styles}>Areas</th> 
        <th style = {styles}>Courses</th>
        {itemstable}
        {completed()}
      </table>
    </div>
    );
  }
}

module.exports = CourseList;