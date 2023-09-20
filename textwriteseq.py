    for place, group in finalseatmap.items():
        sep = " "*20
        if place in pos:
            if place in foran:
                t = place +"\n"
                for i in group:
                    t += i + " "
                t += " |" + sep
                rows[0] += t
            
            elif place in midten:
                t = place+"\n"
                for i in group:
                    t += i + " "
                t += " |" + sep
                rows[1] += t
            
            elif place in bak:
                t = place+"\n"
                for i in group:
                    t += i + " "
                t += " |" + sep
                rows[2] += t