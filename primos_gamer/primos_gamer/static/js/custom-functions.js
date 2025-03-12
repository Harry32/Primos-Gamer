function montarSlider(idSlider, idMinValor, idMaxValor=null, valorMin=0, valorMax=100, step=5){
    let startValues = []
    let startMinValue = document.getElementById(idMinValor).value

    startValues.push(startMinValue);

    if(idMaxValor != null){
        let startMaxValue = document.getElementById(idMaxValor).value

        startValues.push(startMaxValue);
    }

    noUiSlider.create(document.getElementById(idSlider), {
        start: startValues,
        step: step,
        connect: true,
        tooltips: true,
        range: {
            min: valorMin,
            max: valorMax
        },
        pips: {
            mode: "range",
            density: 5,
            stepped: true
        }
    }).on('update', function (values, handle, unencoded, tap, positions, noUiSlider) {
        let minValue = unencoded[0]
        let maxValue = unencoded[1]

        document.getElementById(idMinValor).value = minValue;
        document.getElementById(idMaxValor).value = maxValue;
    });
}