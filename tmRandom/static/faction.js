function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

let colors = ["Green",
    "Black",
    "Brown",
    "Gray",
    "Blue",
    "Red",
    "Yellow",
    "Ice",
    "Volcano",
    "Variable"
];


function get_color(player) {
    shuffle(colors);

    let draw = colors.pop();
    let accept = confirm(player + " drew " + draw + ". Accept?")

    while (accept != true) {

        colors.push(draw);
        shuffle(colors);

        draw = colors.pop();

        accept = confirm(player + " drew " + draw + ". Accept?");
    }
    $("#factions").append("<tr><td>" + player + "</td><td>" + draw + "</td></tr>");

    if (["Ice", "Variable"].includes(draw)) {
        let temp = [];
        const expansions = ["Ice", "Volcano", "Variable"];
        expansions.forEach(function(item, index, array) {
            {
            const i = colors.indexOf(item);
                if (i > -1)
                {
                    colors.splice(i, 1);
                    temp.push(item);
                }
            }
            console.log("Temp array: " + temp);

        });

        colors.sort();

        let choice = prompt(player + " drew " + draw + ".\nChoose a terrain color:\n" + colors.join(", "));
        while (choice == null || choice == '') {
            choice = prompt("That is not a valid terrain option. Please try again." + ".\nChoose a terrain color:\n" + colors.join(", "));
        }

        let exists = colors.indexOf(choice[0].toUpperCase() + choice.slice(1).toLowerCase())

        while (exists == -1) {
            choice = prompt("That is not a valid terrain option. Please try again." + ".\nChoose a terrain color:\n" + colors.join(", "));
            exists = colors.indexOf(choice[0].toUpperCase() + choice.slice(1).toLowerCase())
        }
        colors.splice(exists, 1)
        colors = colors.concat(temp)

        $("td:last").append(" | " + choice[0].toUpperCase() + choice.slice(1).toLowerCase())

    }

}

let players = $("#players").text().split(", ");

$("#faction").click(function() {
    players.forEach(function(item, index, array) {
        get_color(item)
    });

    $("#faction").hide();
    $("#redraw").show();

});

$("#redraw").click(function() {
    colors = ["Green", "Black", "Brown", "Gray", "Blue", "Red", "Yellow", "Ice", "Volcano", "Variable"];

    $("#factions tr").remove()

    players.forEach(function(item, index, array) {
        get_color(item)
    });

});

