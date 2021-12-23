$("#tamano").on('change', function() {
    // Aqui va la llamada AJAX con JQuery
    $.ajax({
        url: "/checksize",
        data: {
            size: this.value
        },
        success: function(data, textStatus, jqXHR) {
            verificar_tamaño_pizza(data.estado)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert("Error");
        }
    });
});

function verificar_tamaño_pizza(estado) {
    if (estado) {
        $("#resultado_tamano").text("Disponible");
        $("#resultado_tamano").css("color", "green");
    } else {
        $("#resultado_tamano").text("No Disponible");
        $("#resultado_tamano").css("color", "red");
    }
}