from database import Database

def main():
    db = Database() 
    #db.print_all_titles()
    #db.print_all_companies()
    db.get_vote_average("Avatar")
    db.get_revenue("Avatar")
    db.get_proco_name("Avatar")
    db.get_proco_founder("Avatar")

main()
