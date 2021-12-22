var vtb = new Map()
    vtb.set("thous50",0.02);
    var sber = new Map()
    sber.set("thous50",0.01);
    var slovarznach={
        vtb:{

            thous50:1.02,
            thous100:1.03,
            thous200:1.04
        },

        sber:{

            thous50:1.01,
            thous100:1.02,
            thous200:1.03
        },

        alfa:{

            thous50:1.04,
            thous100:1.05,
            thous200:1.06,
        }
    }
    function summaproc(bank,vklad,years,save){
        var itog=0
        if (years==""){
            alert("Введите количество лет")
        }
        else{
            if (vklad=="thous50"){
                    itog=50000
                }
                else if (vklad=="thous100"){
                    itog=100000
                }
                else if (vklad=="thous200"){
                    itog=20000
                }
            for (var i=0;i<years;i++){
                if (vklad=="thous50"){
                    if (bank=="sber"){
                        itog*=slovarznach.sber.thous50
                    }
                    else if (bank=="vtb"){
                        itog*=slovarznach.vtb.thous50
                    }
                    else if (bank=="alfa"){
                        itog*=slovarznach.alfa.thous50
                    }
                }
                else if (vklad=="thous100"){
                    if (bank=="sber"){
                        itog*=slovarznach.sber.thous100
                    }
                    else if (bank=="vtb"){
                        itog*=slovarznach.vtb.thous100
                    }
                    else if (bank=="alfa"){
                        itog*=slovarznach.alfa.thous100
                    }
                }
                else if (vklad=="thous200"){
                    if (bank=="sber"){
                        itog*=slovarznach.sber.thous200
                    }
                    else if (bank=="vtb"){
                        itog*=slovarznach.vtb.thous200
                    }
                    else if (bank=="alfa"){
                        itog*=slovarznach.alfa.thous200
                    }
                }
            }
            if (save){
            alert(itog.toFixed(2))
            }
            else{
                localStorage.setItem("summaProc",itog.toFixed(2));
                alert("Сохранено в localStorage");
                alert(localStorage.getItem("summaProc"))
            }
        }
    }
