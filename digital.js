 function updateClock(){

  const now = new Date();
  let hours = now.getHours();
  const meridiem = hours >= 12? "PM" : "AM";
  hours = hours % 12|| 12;
  hours = hours.toString();
  const minutes = now.getMinutes().toString();
  const seconds = now.getSeconds().toString();
  const timestring = `${hours}:${minutes}:${seconds}:${meridiem}`;
  document.getElementById("clock").textContent =  timestring

 }

 updateClock();
 setInterval(updateClock,1000);
 