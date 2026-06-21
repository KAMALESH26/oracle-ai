import Sidebar from "./Sidebar";

function MainLayout({ children }) {

  return (

    <div className="layout">

      <Sidebar />

      <div className="content">

        {children}

      </div>

    </div>
  );
}

export default MainLayout;