import React, { useEffect, useState } from 'react';
import { PlusOutlined } from '@ant-design/icons';
import {
    Form,
    Input,
    Button,
    Radio,
    Select,
    Cascader,
    DatePicker,
    InputNumber,
    TreeSelect,
    Switch,
    Checkbox,
    Upload,
    Typography,
    Layout,
    Space,
    Row,
    Col,
    Image,
    Card
} from 'antd';
import { useNavigate, useParams } from 'react-router-dom';

const { Title, Paragraph, Text, Link } = Typography;

const { RangePicker } = DatePicker;
const { TextArea } = Input;


export function VariantDetail() {
    const { variantId } = useParams()
    const [variant, setVariant] = useState({})

    useEffect(() => {
        fetch(`http://localhost:9000/variant/${variantId}`, {
            "methods": "GET",
            headers: {
                "Content-Type": "applications/json"
            }
        }).then(resp => resp.json())
        .then(resp => setVariant(resp))
        .catch(error => console.error(error))
    }, [])

    let navigate = useNavigate();
    const navigateHome = () => {
        navigate("/");
    };

    return (
        <>
            <Layout style={{background: "#303e45", color: "#bfced6", cursor: 'pointer'}}>
            <Title style={{color: "#bfced6", fontFamily: 'courier', cursor: 'pointer'}} onClick={navigateHome}>
                    <center>Simple Marketplace</center>
                </Title>
            </Layout>

            <Layout>
                <Title><center>{variant.name}</center></Title>
                <Space direction='vertical'>
                    <Row justify='center'>
                        {variant.images?.map(vim => {
                            return (
                                <Col key={vim.id}>
                                    <Image height={200} src={vim.image_url?vim.image_url:"data:image/png;base64,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"}/>
                                </Col>
                            )
                        })}
                    </Row>

                    <Card title='Color'>
                        <p>{variant.color}</p>
                    </Card>
                    <Card title='Size'>
                        <p>{variant.size}</p>
                    </Card>
                </Space>
            </Layout>
        </>
    )
}


export function CreateVariant() {
    let navigate = useNavigate();
    const navigateHome = () => {
        navigate("/");
    };
    return (
        <>
        <Form
            labelCol={{
                span: 4,
            }}
            wrapperCol={{
                span: 14,
            }}
            layout="horizontal"
        >
            <Layout style={{background: "#303e45", color: "#bfced6"}}>
            <Title style={{color: "#bfced6", fontFamily: 'courier', cursor: 'pointer'}} onClick={navigateHome}>
                    <center>Simple Marketplace</center>
                </Title>
            </Layout>
            <h1><center>Create Variant</center></h1>

            <Form.Item label="Variant Name">
            <Input disabled={true} value="variant name"/>
            </Form.Item>

            <Form.Item label="Variant Name">
            <Input/>
            </Form.Item>

            <Form.Item label="Variant Color">
            <Input/>
            </Form.Item>

            <Form.Item label="Variant Size">
            <Input/>
            </Form.Item>

            <h4><center>*On the next page you will need to fill some extra details for your variant</center></h4>

            <Row justify='center'>
                <Space direction='horizontal' size='small'>
                    <Button
                        type='primary'
                        onClick={
                            () => {console.log("weey");
                        }}
                    >
                        save
                    </Button>
                </Space>
            </Row>
        </Form>
        </>
    );
};


export function UpdateVariant() {
    let navigate = useNavigate();
    const navigateHome = () => {
        navigate("/");
    };
    return (
        <>
        <Form
            labelCol={{
                span: 4,
            }}
            wrapperCol={{
                span: 14,
            }}
            layout="horizontal"
        >
            <Layout style={{background: "#303e45", color: "#bfced6"}}>
            <Title style={{color: "#bfced6", fontFamily: 'courier', cursor: 'pointer'}} onClick={navigateHome}>
                    <center>Simple Marketplace</center>
                </Title>
            </Layout>
            <p></p>
            <h1><center>Update Variant</center></h1>

            <Form.Item label="Variant Name">
            <Input disabled={true} value="variant name"/>
            </Form.Item>

            <Form.Item label="Variant Name">
            <Input/>
            </Form.Item>

            <Form.Item label="Variant Color">
            <Input/>
            </Form.Item>

            <Form.Item label="Variant Size">
            <Input/>
            </Form.Item>

            <Form.Item label="Variant Images" valuePropName="fileList">
                <Upload action="/upload.do" listType="picture-card">
                    <div>
                        <PlusOutlined />
                        <div
                            style={{
                                marginTop: 8,
                            }}
                        >
                            Upload
                        </div>
                    </div>
                </Upload>
            </Form.Item>

            <Row justify='center'>
                <Space direction='horizontal' size='small'>
                    <Button
                        type='primary'
                        onClick={
                            () => {console.log("weey");
                        }}
                    >
                        save
                    </Button>

                    <Button
                        type='primary'
                        onClick={
                            () => {console.log("weey");
                        }}
                        style={{background: 'red'}}
                    >
                        delete
                    </Button>
                </Space>
            </Row>
        </Form>
        </>
    );
};
