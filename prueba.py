fecha = new Date(prompt('Ingrese su fecha de nacimiento', 'mm/dd/yyyy'));
hoy = new Date();
if(fecha.getMonth == hoy.getMonth)
    if(fecha.getDate < hoy.getDate)
    document.write('<h1> 1Usted tiene ' +(hoy.getFullYear - fecha.getFullYear) + ' años con '
                   + (hoy.getDate - fecha.getDate) + ' dias </h1>')
    else
        document.write('<h1> 2Usted tiene ' +(hoy.getFullYear - fecha.getFullYear) + ' años con '
                       + (fecha.getDate - hoy.getDate) + ' dias </h1>')        
else
    if(fecha.getMonth > hoy.getMonth)
        	if(fecha.getDate > hoy.getDate)
                    document.write('<h1> 3Usted tiene ' +(hoy.getFullYear - fecha.getFullYear)
                                   + ' años con ' + (fecha.getMonth - hoy.getMonth) + ' meses y ' +
                                   (fecha.getDate - hoy.getDate) + ' dias </h1>')
        	else
          	document.write('<h1> 4Usted tiene ' +(hoy.getFullYear - fecha.getFullYear) +
                               ' años con ' + (fecha.getMonth - hoy.getMonth) + ' meses y ' +
                               (hoy.getDate - fecha.getDate) + ' dias </h1>')
    else
        if(fecha.getMonth < hoy.getMonth)
        	if(fecha.getDate > hoy.getDate)
        		document.write('<h1>5 Usted tiene ' +
                                       (hoy.getFullYear - fecha.getFullYear) + ' años con ' +
                                       (hoy.getMonth - fecha.getMonth) + ' meses y ' +
                                       (fecha.getDate - hoy.getDate) + ' dias </h1>')
        	else
          	document.write('<h1>6 Usted tiene ' +(hoy.getFullYear - fecha.getFullYear) + ' años con ' + (fecha.getMonth - hoy.getMonth) + ' meses y ' +(hoy.getDate - fecha.getDate) + ' dias </h1>')
          
        
      
