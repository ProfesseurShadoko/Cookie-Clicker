from cookie_clicker import CookieClicker
from stats import update_stats,show_cc_stats,show_stats



if __name__=="__main__":
    cc = CookieClicker()
    cc.run()
    
    update_stats(cc)
    show_cc_stats(cc)
    print()
    show_stats()
