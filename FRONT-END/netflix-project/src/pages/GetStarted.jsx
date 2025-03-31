import { ChevronRightIcon } from "lucide-react";

function GetStarted() {
  return (
    <div className="bg-black h-screen">
        <div className="bg-[url('/src/assets/fundocadastronetflix.jpg')] bg-cover w-screen bg-center h-190 relative ">
        <div className="absolute inset-0 bg-gradient-to-t from-transparent to-black/100"></div>
        <div className="absolute inset-0 bg-gradient-to-t from-black/100 to-transparent"></div>
        <div className="h-30 w-screen absolute flex items-center justify-between">
            <img src="src/assets/netflix-logo.png" className="-mt-10 sm:ml-0 md:ml-15 lg:ml-30 h-full object-contain object-left"/>
            <button className="-mt-10 mr-10 sm:mr-10 md:mr-20 lg:mr-35 p-1.5 w-25 bg-red-600 text-white rounded-md text-sm"><b>Sign In</b></button>
        </div>
        <div className="flex items-center justify-center h-full">
            <div className="relative inset-0 flex flex-col items-center justify-center w-150 text-white text-center">
                <h1 className="text-lg sm:text-6xl font-bold mb-4 ">Unlimited movies, TV shows, and more.</h1>
                <h2 className="sm:text-1xl font-bold mb-6">Starts at BRL20.90. Cancel anytime.</h2>
                <p className="text-xs sm:text-1xl mb-4">Ready to watch? Enter your email to create or restart your membership.</p>
                <div className="flex">
                <input type="email" placeholder="Email address" className="mr-3 p-3 w-50 md:w-80 rounded-md mb-4 ring-1 ring-gray-400 focus:outline-2 focus:outline-gray-50 h-14"/>
                <button className="text-2xl bg-red-600 text-white p-1 md:p-3 rounded-md w-40 md:w-50 h-14 md:h-full flex hover:bg-red-700 items-center"><b className="mr-2 md:mr-3  text-lg md:text-2xl">Get Started</b><ChevronRightIcon size={30} style={{height: '34px'}}/></button>
                </div>
            </div>
        </div>
        </div>
    </div>
  );
}
export default GetStarted;