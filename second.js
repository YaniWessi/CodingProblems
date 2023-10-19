return (
  <header className="bg-gray-800 py-4 px-6 text-white">
    <div className="flex items-center justify-between">





      <div className="flex items-center">



      
        <div className="mr-4">
          {isSearchVisible ? (
            <input
              type="text"
              className="bg-gray-700 rounded-full py-2 px-4 text-sm text-gray-200 focus:outline-none focus:bg-gray-600 w-full"
              placeholder="Search"
            />
          ) : (
            <button
              className="block focus:outline-none text-white text-xl"
              onClick={toggleSearch}
            >
              <MdSearch className="md:hidden" />
              <FaPlusSquare className="hidden md:block" onClick={toggleSearch} />
            </button>
          )}
        </div>




        <div className="hidden md:block">
          <FaRegBell className="mr-4 text-xl" />
          <FaRegClone className="mr-4 text-xl" />
        </div>

      </div>



















      <div className="flex items-center">


        <div className="relative inline-block">


          <button
            className="flex items-center focus:outline-none"
            onClick={toggleDropdown}
          >
            <img
              src={profileImage}
              alt="Profile"
              className="w-8 h-8 rounded-full mr-2"
            />
            <span>John Doe</span>
            <IoMdArrowDropdown className="ml-2" />
          </button>

          
          {isDropdownOpen && (
            <div className="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
              <div className="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">View Profile</a>
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Settings</a>
                <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Logout</a>
              </div>
            </div>
          )}



        </div>



      </div>





    </div>
  </header>
);