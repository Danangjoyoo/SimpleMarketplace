import { Route, Routes } from "react-router-dom"
import { Home } from "./pages/Home";
import { CreateProduct, ProductDetail, UpdateProduct } from "./pages/Product";
import { CreateVariant, UpdateVariant, VariantDetail } from "./pages/Variant";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/product/:productId" element={<ProductDetail/>} />
      <Route path="/product/add" element={<CreateProduct/>} />
      <Route path="/product/update/:productId" element={<UpdateProduct/>} />
      <Route path="/variant/:variantId" element={<VariantDetail/>} />
      <Route path="/variant/add/:productId" element={<CreateVariant/>} />
      <Route path="/variant/update/:variantId" element={<UpdateVariant/>} />
    </Routes>
  )
}

export default App;
