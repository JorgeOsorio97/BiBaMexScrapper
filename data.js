var data = [
  {
    id: 1,
    nombre: "PIB",
    formula_o: "pib/perritos",
    formula: "id1/id2",
    tipo: "serial",
    descripcion: "asdsad",
  },
  {
    id: 2,
    nombre: "Tarjetas de Credito",
    formula_o: "pib/perritos",
    formula: "id1/id2",
    tipo: "serial",
    descripcion: "asdsad",
  },
  {
    id: 3,
    nombre: "Acaparación mercado",
    formula_o: "pib/perritos",
    formula: "id1/id2",
    tipo: "serial",
    descripcion: "asdsad",
  },
  {
    id: 4,
    nombre: "Prueba",
    formula_o: "pib/perritos",
    formula: "id1/id2",
    tipo: "serial",
    descripcion: "asdsad",
  },
];

const estados = {
  fips: 797010,
  estado: "rox",
  municipio: "municipio",
  valor_principal: 0.5,
  otros_valores: [
    {
      nombre: "TC",
      valor: 5,
    },
    {
      nombre: "PIB",
      valor: 3,
    },
  ],
};

stateData.map((val)=>{
    return {
        fips: val.properties.POB1,
        municipio: val.properties.NOM_MUN,
        valor_principal = Math.random()
    }
})

const indicadores = [
    {
        id: 1,
        nombre: "INFLACION",
        fuente: "CNBV",
        g_tiempo: "mensual",
        g_espacio: "pais",
        descripcion: ""
    },
    {
        id: 2,
        nombre: "TIIE",
        fuente: "CNBV",
        g_tiempo: "anual",
        g_espacio: "pais",
        descripcion: ""
    },
    {
        id: 3,
        nombre: "Remuneraciones Manufacturares",
        fuente: "CNBV",
        g_tiempo: "anual",
        g_espacio: "ciudad",
        descripcion: ""
    },
    {
        id: 4,
        nombre: "Composición de la población económicamente activa",
        fuente: "CNBV",
        g_tiempo: "anual",
        g_espacio: "ciudad",
        descripcion: ""
    }
]


let treemap1 = [
    {
        'estado':'MEX',
        'tamano':1.5,
        'color':2
    },
    {
        'estado':'AGUAS',
        'tamano':3.2,
        'color':10
    },

]