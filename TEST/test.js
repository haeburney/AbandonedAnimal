function fetchData() {
  return new Promis(function (receive)
    fetch("sample.json")  
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      receive(JSON.stringify(data));
    });
  });
}

(async function () {
  jsonData = await fetchData();
  $(".hetJson").text(jsonData);
})
