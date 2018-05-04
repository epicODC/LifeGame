'''
def set_data_delaberate():
    file_pathname
    data = np.loadtxt(file_pathname)

    file_path = 'init_data_deleberate/' + \
                 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    np.savetxt(file_path, data, fmt="%d")
    np.savetxt('.lifedata', data, fmt="%d")
    #np.loadtxt(file_pathname, delimiter="  ") 
    return 
  
def set_data_random():
  init_size, init_possiblity = get_init_info()
  #some tricks to random generate the life with player's chioce
  random_select_list = range(init_size*init_size)
  data = [([0] * size+2) for i in range(size+2)]
  gap_distance = int((size - init_size) / 2)
  for select_row_num in range(gap_distance, gap_distance+init_size):
    for select_column_num in range(gap_distance, gap_distance+init_size):
      select_num = random.choice(random_select_list)
      random_select_list.remove(select_num)
      if select_num < int(init_possiblity*init_size*init_size):
        data[select_row_num][select_column_num] = LifeData.kLive
      else:
        data[select_row_num][select_column_num] = LifeData.kDie
  #save the data in a file
  file_path = 'init_data_random/'+ \
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + \
               '[' + chr(init_size) + ', ' + chr(init_possiblity) + ']'
  np.savetxt(file_path, data, fmt="%d")
  np.savetxt('.lifedata', data, fmt="%d")
  #np.loadtxt(file_pathname) 
  return

def get_data():
  get_data_handle = Tk()
  choice_frame = Frame(get_data_handle)
  choice_label = Label(choice_frame, 
                       text = 'select the mode', 
                       font = 'time 20 bold')
  choice_label.grid(row = 1, column = 1)
  choice_button_random = Button(choice_frame, 
                                text = 'Random', 
                                font = 'time 20 bold',
                                command = set_data_random)
  choice_button_random.grid(row = 2, column = 1)
  choice_button_deliberate = Button(choice_frame, 
                                text = 'Deliberate', 
                                font = 'time 20 bold',
                                command = set_data_delaberate)
  choice_button_deliberate.grid(row = 3, column = 1)
  
  data = np.loadtxt('.lifedata',fmt="%d") 
  return data
'''